import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_VolumeFlowIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und VolumeFlowIndicator
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'VolumeFlowIndicator': {
                'class': VolumeFlowIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeFlowIndicator'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'VolumeFlowIndicator': 1.0
        })
    )
