import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
