import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und BarStrength
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'BarStrength': 1.0
        })
    )
