import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und BarStrength
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'BarStrength': 1.0
        })
    )
