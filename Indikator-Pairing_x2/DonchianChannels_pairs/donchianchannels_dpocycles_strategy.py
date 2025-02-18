import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und DPOCycles
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'DPOCycles': 1.0
        })
    )
