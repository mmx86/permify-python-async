# coding: utf-8

"""
    Permify API

    Permify is an open source authorization service for creating fine-grained and scalable authorization systems.

    The version of the OpenAPI document: v0.8.7
    Contact: hello@permify.co
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from permify_async.models.checked_expr import CheckedExpr

class TestCheckedExpr(unittest.TestCase):
    """CheckedExpr unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CheckedExpr:
        """Test CheckedExpr
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CheckedExpr`
        """
        model = CheckedExpr()
        if include_optional:
            return CheckedExpr(
                reference_map = {
                    'key' : permify_async.models.v1alpha1/reference.v1alpha1.Reference(
                        name = '', 
                        overload_id = [
                            ''
                            ], 
                        value = permify_async.models.constant.Constant(
                            null_value = '', 
                            bool_value = True, 
                            int64_value = '', 
                            uint64_value = '', 
                            double_value = 1.337, 
                            string_value = '', 
                            bytes_value = 'YQ==', 
                            duration_value = '', 
                            timestamp_value = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), )
                    },
                type_map = {
                    'key' : permify_async.models.v1alpha1/type.v1alpha1.Type(
                        dyn = permify_async.models.dyn.dyn(), 
                        null = '', 
                        primitive = 'PRIMITIVE_TYPE_UNSPECIFIED', 
                        wrapper = 'PRIMITIVE_TYPE_UNSPECIFIED', 
                        well_known = 'WELL_KNOWN_TYPE_UNSPECIFIED', 
                        list_type = permify_async.models.list_type.ListType(
                            elem_type = permify_async.models.v1alpha1/type.v1alpha1.Type(
                                dyn = permify_async.models.dyn.dyn(), 
                                null = '', 
                                map_type = permify_async.models.map_type.MapType(
                                    key_type = , 
                                    value_type = , ), 
                                function = permify_async.models.function_type.FunctionType(
                                    result_type = , 
                                    arg_types = [
                                        
                                        ], ), 
                                message_type = '', 
                                type_param = '', 
                                type = , 
                                error = permify_async.models.error.error(), 
                                abstract_type = permify_async.models.abstract_type.AbstractType(
                                    name = '', 
                                    parameter_types = [
                                        
                                        ], ), ), ), 
                        map_type = permify_async.models.map_type.MapType(), 
                        function = permify_async.models.function_type.FunctionType(), 
                        message_type = '', 
                        type_param = '', 
                        type = , 
                        error = permify_async.models.error.error(), 
                        abstract_type = permify_async.models.abstract_type.AbstractType(
                            name = '', ), )
                    },
                source_info = permify_async.models.source_info.SourceInfo(
                    syntax_version = '', 
                    location = '', 
                    line_offsets = [
                        56
                        ], 
                    positions = {
                        'key' : 56
                        }, 
                    macro_calls = {
                        'key' : permify_async.models.expr.Expr(
                            id = '', 
                            const_expr = permify_async.models.constant.Constant(
                                null_value = '', 
                                bool_value = True, 
                                int64_value = '', 
                                uint64_value = '', 
                                double_value = 1.337, 
                                string_value = '', 
                                bytes_value = 'YQ==', 
                                duration_value = '', 
                                timestamp_value = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                            ident_expr = permify_async.models.ident.Ident(
                                name = '', ), 
                            select_expr = permify_async.models.select.Select(
                                operand = permify_async.models.expr.Expr(
                                    id = '', 
                                    call_expr = permify_async.models.expr/call.Expr.Call(
                                        target = , 
                                        function = '', 
                                        args = [
                                            
                                            ], ), 
                                    list_expr = permify_async.models.create_list.CreateList(
                                        elements = [
                                            
                                            ], 
                                        optional_indices = [
                                            56
                                            ], ), 
                                    struct_expr = permify_async.models.create_struct.CreateStruct(
                                        message_name = '', 
                                        entries = [
                                            permify_async.models.entry.Entry(
                                                id = '', 
                                                field_key = '', 
                                                map_key = , 
                                                value = , 
                                                optional_entry = True, )
                                            ], ), 
                                    comprehension_expr = permify_async.models.comprehension.Comprehension(
                                        iter_var = '', 
                                        iter_range = , 
                                        accu_var = '', 
                                        accu_init = , 
                                        loop_condition = , 
                                        loop_step = , 
                                        result = , ), ), 
                                field = '', 
                                test_only = True, ), 
                            call_expr = permify_async.models.expr/call.Expr.Call(
                                function = '', ), 
                            list_expr = permify_async.models.create_list.CreateList(), 
                            struct_expr = permify_async.models.create_struct.CreateStruct(
                                message_name = '', ), 
                            comprehension_expr = permify_async.models.comprehension.Comprehension(
                                iter_var = '', 
                                accu_var = '', ), )
                        }, ),
                expr_version = '',
                expr = permify_async.models.expr.Expr(
                    id = '', 
                    const_expr = permify_async.models.constant.Constant(
                        null_value = '', 
                        bool_value = True, 
                        int64_value = '', 
                        uint64_value = '', 
                        double_value = 1.337, 
                        string_value = '', 
                        bytes_value = 'YQ==', 
                        duration_value = '', 
                        timestamp_value = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                    ident_expr = permify_async.models.ident.Ident(
                        name = '', ), 
                    select_expr = permify_async.models.select.Select(
                        operand = permify_async.models.expr.Expr(
                            id = '', 
                            call_expr = permify_async.models.expr/call.Expr.Call(
                                target = , 
                                function = '', 
                                args = [
                                    
                                    ], ), 
                            list_expr = permify_async.models.create_list.CreateList(
                                elements = [
                                    
                                    ], 
                                optional_indices = [
                                    56
                                    ], ), 
                            struct_expr = permify_async.models.create_struct.CreateStruct(
                                message_name = '', 
                                entries = [
                                    permify_async.models.entry.Entry(
                                        id = '', 
                                        field_key = '', 
                                        map_key = , 
                                        value = , 
                                        optional_entry = True, )
                                    ], ), 
                            comprehension_expr = permify_async.models.comprehension.Comprehension(
                                iter_var = '', 
                                iter_range = , 
                                accu_var = '', 
                                accu_init = , 
                                loop_condition = , 
                                loop_step = , 
                                result = , ), ), 
                        field = '', 
                        test_only = True, ), 
                    call_expr = permify_async.models.expr/call.Expr.Call(
                        function = '', ), 
                    list_expr = permify_async.models.create_list.CreateList(), 
                    struct_expr = permify_async.models.create_struct.CreateStruct(
                        message_name = '', ), 
                    comprehension_expr = permify_async.models.comprehension.Comprehension(
                        iter_var = '', 
                        accu_var = '', ), )
            )
        else:
            return CheckedExpr(
        )
        """

    def testCheckedExpr(self):
        """Test CheckedExpr"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
