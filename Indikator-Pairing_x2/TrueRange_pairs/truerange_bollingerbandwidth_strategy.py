import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRange_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRange und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'TrueRange': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
