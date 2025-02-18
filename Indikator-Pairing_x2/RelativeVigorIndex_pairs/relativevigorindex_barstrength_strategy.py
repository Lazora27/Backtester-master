import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVigorIndex_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVigorIndex und BarStrength
    """
    
    params = (
        ('indicators', {
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'RelativeVigorIndex': 1.0,
            'BarStrength': 1.0
        })
    )
