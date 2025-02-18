import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'AccelerationBands': 1.0
        })
    )
