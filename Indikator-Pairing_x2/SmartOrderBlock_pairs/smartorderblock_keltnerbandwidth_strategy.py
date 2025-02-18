import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
