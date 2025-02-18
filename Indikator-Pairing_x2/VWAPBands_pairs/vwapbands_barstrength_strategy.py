import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und BarStrength
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'BarStrength': 1.0
        })
    )
