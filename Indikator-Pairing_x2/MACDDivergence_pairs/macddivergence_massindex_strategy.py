import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und MassIndex
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'MassIndex': 1.0
        })
    )
