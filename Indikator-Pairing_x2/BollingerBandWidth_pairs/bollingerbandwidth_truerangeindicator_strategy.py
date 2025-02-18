import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandWidth_TrueRangeIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandWidth und TrueRangeIndicator
    """
    
    params = (
        ('indicators', {
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            },
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            }
        }),
        ('weights', {
            'BollingerBandWidth': 1.0,
            'TrueRangeIndicator': 1.0
        })
    )
