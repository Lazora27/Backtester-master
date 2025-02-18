import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
