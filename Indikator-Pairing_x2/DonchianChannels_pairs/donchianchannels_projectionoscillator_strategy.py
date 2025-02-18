import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'ProjectionOscillator': 1.0
        })
    )
