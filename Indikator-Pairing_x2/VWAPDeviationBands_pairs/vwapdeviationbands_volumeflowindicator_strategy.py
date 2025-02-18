import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPDeviationBands_VolumeFlowIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPDeviationBands und VolumeFlowIndicator
    """
    
    params = (
        ('indicators', {
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            },
            'VolumeFlowIndicator': {
                'class': VolumeFlowIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeFlowIndicator'>
            }
        }),
        ('weights', {
            'VWAPDeviationBands': 1.0,
            'VolumeFlowIndicator': 1.0
        })
    )
