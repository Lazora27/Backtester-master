import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_GannFans_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und GannFans
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'GannFans': 1.0
        })
    )
