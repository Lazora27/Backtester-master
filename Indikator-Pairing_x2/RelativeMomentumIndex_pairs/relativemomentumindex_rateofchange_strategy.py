import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeMomentumIndex_RateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeMomentumIndex und RateOfChange
    """
    
    params = (
        ('indicators', {
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            },
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            }
        }),
        ('weights', {
            'RelativeMomentumIndex': 1.0,
            'RateOfChange': 1.0
        })
    )
