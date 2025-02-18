import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVigorIndex_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVigorIndex und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'RelativeVigorIndex': 1.0,
            'SeasonalStrength': 1.0
        })
    )
