import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BuyingPressure_VolumeFlowIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BuyingPressure und VolumeFlowIndicator
    """
    
    params = (
        ('indicators', {
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            },
            'VolumeFlowIndicator': {
                'class': VolumeFlowIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeFlowIndicator'>
            }
        }),
        ('weights', {
            'BuyingPressure': 1.0,
            'VolumeFlowIndicator': 1.0
        })
    )
