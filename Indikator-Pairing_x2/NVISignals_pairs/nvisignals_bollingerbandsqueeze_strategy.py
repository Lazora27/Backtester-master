import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_BollingerBandSqueeze_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und BollingerBandSqueeze
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'BollingerBandSqueeze': 1.0
        })
    )
