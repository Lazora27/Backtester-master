import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_BollingerBandSqueeze_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und BollingerBandSqueeze
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'BollingerBandSqueeze': 1.0
        })
    )
