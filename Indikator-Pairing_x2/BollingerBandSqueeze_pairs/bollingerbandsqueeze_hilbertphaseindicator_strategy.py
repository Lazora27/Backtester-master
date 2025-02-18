import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandSqueeze_HilbertPhaseIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandSqueeze und HilbertPhaseIndicator
    """
    
    params = (
        ('indicators', {
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            },
            'HilbertPhaseIndicator': {
                'class': HilbertPhaseIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertPhaseIndicator'>
            }
        }),
        ('weights', {
            'BollingerBandSqueeze': 1.0,
            'HilbertPhaseIndicator': 1.0
        })
    )
