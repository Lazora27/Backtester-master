import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'DonchianChannels': 1.0
        })
    )
