import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandSqueeze_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandSqueeze und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'BollingerBandSqueeze': 1.0,
            'PhaseDivergence': 1.0
        })
    )
