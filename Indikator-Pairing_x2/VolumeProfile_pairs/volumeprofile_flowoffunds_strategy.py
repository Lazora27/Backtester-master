import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'FlowOfFunds': 1.0
        })
    )
