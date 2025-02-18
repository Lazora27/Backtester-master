import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_VolumeFlowIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und VolumeFlowIndicator
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'VolumeFlowIndicator': {
                'class': VolumeFlowIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeFlowIndicator'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'VolumeFlowIndicator': 1.0
        })
    )
