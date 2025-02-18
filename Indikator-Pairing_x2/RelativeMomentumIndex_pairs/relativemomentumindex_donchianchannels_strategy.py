import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeMomentumIndex_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeMomentumIndex und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'RelativeMomentumIndex': 1.0,
            'DonchianChannels': 1.0
        })
    )
