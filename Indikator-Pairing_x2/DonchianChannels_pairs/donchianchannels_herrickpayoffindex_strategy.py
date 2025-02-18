import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_HerrickPayoffIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und HerrickPayoffIndex
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'HerrickPayoffIndex': {
                'class': HerrickPayoffIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HerrickPayoffIndex'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'HerrickPayoffIndex': 1.0
        })
    )
