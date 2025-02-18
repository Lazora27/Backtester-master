import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
