import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderFlowVolumeProfile_AccumulationDistributionLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderFlowVolumeProfile und AccumulationDistributionLine
    """
    
    params = (
        ('indicators', {
            'OrderFlowVolumeProfile': {
                'class': OrderFlowVolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderFlowVolumeProfile'>
            },
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            }
        }),
        ('weights', {
            'OrderFlowVolumeProfile': 1.0,
            'AccumulationDistributionLine': 1.0
        })
    )
