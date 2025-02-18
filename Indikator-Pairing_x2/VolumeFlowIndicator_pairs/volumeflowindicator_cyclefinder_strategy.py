import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeFlowIndicator_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeFlowIndicator und CycleFinder
    """
    
    params = (
        ('indicators', {
            'VolumeFlowIndicator': {
                'class': VolumeFlowIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeFlowIndicator'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'VolumeFlowIndicator': 1.0,
            'CycleFinder': 1.0
        })
    )
