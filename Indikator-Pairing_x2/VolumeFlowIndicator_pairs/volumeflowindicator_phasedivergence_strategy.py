import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeFlowIndicator_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeFlowIndicator und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'VolumeFlowIndicator': {
                'class': VolumeFlowIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeFlowIndicator'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'VolumeFlowIndicator': 1.0,
            'PhaseDivergence': 1.0
        })
    )
