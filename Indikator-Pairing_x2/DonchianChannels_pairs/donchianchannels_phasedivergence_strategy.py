import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'PhaseDivergence': 1.0
        })
    )
