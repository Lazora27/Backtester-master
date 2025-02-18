import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_VWAPDeviationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und VWAPDeviationBands
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'VWAPDeviationBands': 1.0
        })
    )
