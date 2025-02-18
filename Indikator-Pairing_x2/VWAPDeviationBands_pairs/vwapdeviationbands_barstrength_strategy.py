import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPDeviationBands_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPDeviationBands und BarStrength
    """
    
    params = (
        ('indicators', {
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'VWAPDeviationBands': 1.0,
            'BarStrength': 1.0
        })
    )
