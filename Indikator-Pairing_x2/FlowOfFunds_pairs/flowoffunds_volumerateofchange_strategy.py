import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FlowOfFunds_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FlowOfFunds und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'FlowOfFunds': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
