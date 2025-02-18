import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'BradleySiderograph': 1.0
        })
    )
