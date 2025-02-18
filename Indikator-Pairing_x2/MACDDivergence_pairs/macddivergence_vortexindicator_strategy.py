import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_VortexIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und VortexIndicator
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'VortexIndicator': 1.0
        })
    )
