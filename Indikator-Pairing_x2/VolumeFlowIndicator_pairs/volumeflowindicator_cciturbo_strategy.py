import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeFlowIndicator_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeFlowIndicator und CCITurbo
    """
    
    params = (
        ('indicators', {
            'VolumeFlowIndicator': {
                'class': VolumeFlowIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeFlowIndicator'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'VolumeFlowIndicator': 1.0,
            'CCITurbo': 1.0
        })
    )
