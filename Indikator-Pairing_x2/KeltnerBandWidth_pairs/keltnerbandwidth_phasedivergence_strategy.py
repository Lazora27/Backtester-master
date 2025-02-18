import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerBandWidth_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerBandWidth und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'KeltnerBandWidth': 1.0,
            'PhaseDivergence': 1.0
        })
    )
