import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KaufmanEfficiencyRatio_RelativeStrengthIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KaufmanEfficiencyRatio und RelativeStrengthIndex
    """
    
    params = (
        ('indicators', {
            'KaufmanEfficiencyRatio': {
                'class': KaufmanEfficiencyRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KaufmanEfficiencyRatio'>
            },
            'RelativeStrengthIndex': {
                'class': RelativeStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeStrengthIndex1'>
            }
        }),
        ('weights', {
            'KaufmanEfficiencyRatio': 1.0,
            'RelativeStrengthIndex': 1.0
        })
    )
