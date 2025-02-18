import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_EldersForceIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und EldersForceIndex
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'EldersForceIndex': 1.0
        })
    )
