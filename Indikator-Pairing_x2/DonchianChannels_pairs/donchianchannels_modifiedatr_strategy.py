import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'ModifiedATR': 1.0
        })
    )
