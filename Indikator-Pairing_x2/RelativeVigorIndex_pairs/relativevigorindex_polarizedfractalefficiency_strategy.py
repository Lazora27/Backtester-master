import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVigorIndex_PolarizedFractalEfficiency_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVigorIndex und PolarizedFractalEfficiency
    """
    
    params = (
        ('indicators', {
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            },
            'PolarizedFractalEfficiency': {
                'class': PolarizedFractalEfficiency,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedFractalEfficiency'>
            }
        }),
        ('weights', {
            'RelativeVigorIndex': 1.0,
            'PolarizedFractalEfficiency': 1.0
        })
    )
