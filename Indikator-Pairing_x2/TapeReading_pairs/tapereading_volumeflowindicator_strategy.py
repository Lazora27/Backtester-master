import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_VolumeFlowIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und VolumeFlowIndicator
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'VolumeFlowIndicator': {
                'class': VolumeFlowIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeFlowIndicator'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'VolumeFlowIndicator': 1.0
        })
    )
