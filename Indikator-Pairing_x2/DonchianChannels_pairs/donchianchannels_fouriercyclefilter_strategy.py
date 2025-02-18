import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
