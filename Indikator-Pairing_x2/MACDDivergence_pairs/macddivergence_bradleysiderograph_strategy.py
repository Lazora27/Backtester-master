import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'BradleySiderograph': 1.0
        })
    )
