import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_VolumeFlowIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und VolumeFlowIndicator
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'VolumeFlowIndicator': {
                'class': VolumeFlowIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeFlowIndicator'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'VolumeFlowIndicator': 1.0
        })
    )
