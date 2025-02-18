import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandWidth_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandWidth und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'BollingerBandWidth': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
