import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'AverageTrueRange': 1.0
        })
    )
