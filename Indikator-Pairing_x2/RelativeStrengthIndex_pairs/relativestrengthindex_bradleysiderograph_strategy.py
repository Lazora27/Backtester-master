import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeStrengthIndex_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeStrengthIndex und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'RelativeStrengthIndex': {
                'class': RelativeStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeStrengthIndex1'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'RelativeStrengthIndex': 1.0,
            'BradleySiderograph': 1.0
        })
    )
