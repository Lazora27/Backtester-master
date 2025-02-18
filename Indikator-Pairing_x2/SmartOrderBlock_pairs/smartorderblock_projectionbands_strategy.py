import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'ProjectionBands': 1.0
        })
    )
